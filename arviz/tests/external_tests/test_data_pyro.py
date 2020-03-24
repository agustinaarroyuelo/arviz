# pylint: disable=no-member, invalid-name, redefined-outer-name
import numpy as np
import packaging
import pytest
import torch
import pyro
from pyro.infer import Predictive

from ...data.io_pyro import from_pyro
from ..helpers import (  # pylint: disable=unused-import
    chains,
    check_multiple_attrs,
    draws,
    eight_schools_params,
    load_cached_models,
)


class TestDataPyro:
    @pytest.fixture(scope="class")
    def data(self, eight_schools_params, draws, chains):
        class Data:
            obj = load_cached_models(eight_schools_params, draws, chains, "pyro")["pyro"]

        return Data

    @pytest.fixture(scope="class")
    def predictions_params(self):
        """Predictions data for eight schools."""
        return {
            "J": 8,
            "sigma": np.array([5.0, 7.0, 12.0, 4.0, 6.0, 10.0, 3.0, 9.0]),
        }

    @pytest.fixture(scope="class")
    def predictions_data(self, data, predictions_params):
        """Generate predictions for predictions_params"""
        posterior_samples = data.obj.get_samples()
        model = data.obj.kernel.model
        predictions = Predictive(model, posterior_samples)(
            predictions_params["J"], torch.from_numpy(predictions_params["sigma"]).float()
        )
        return predictions

    def get_inference_data(self, data, eight_schools_params, predictions_data):
        posterior_samples = data.obj.get_samples()
        model = data.obj.kernel.model
        posterior_predictive = Predictive(model, posterior_samples)(
            eight_schools_params["J"], torch.from_numpy(eight_schools_params["sigma"]).float()
        )
        prior = Predictive(model, num_samples=500)(
            eight_schools_params["J"], torch.from_numpy(eight_schools_params["sigma"]).float()
        )
        predictions = predictions_data
        return from_pyro(
            posterior=data.obj,
            prior=prior,
            posterior_predictive=posterior_predictive,
            predictions=predictions,
            coords={
                "school": np.arange(eight_schools_params["J"]),
                "school_pred": np.arange(eight_schools_params["J"]),
            },
            dims={"theta": ["school"], "eta": ["school"], "obs": ["school"]},
            pred_dims={"theta": ["school_pred"], "eta": ["school_pred"], "obs": ["school_pred"]},
        )

    def test_inference_data(self, data, eight_schools_params, predictions_data):
        inference_data = self.get_inference_data(data, eight_schools_params, predictions_data)
        test_dict = {
            "posterior": ["mu", "tau", "eta"],
            "sample_stats": ["diverging"],
            "posterior_predictive": ["obs"],
            "predictions": ["obs"],
            "prior": ["mu", "tau", "eta"],
            "prior_predictive": ["obs"],
        }
        fails = check_multiple_attrs(test_dict, inference_data)
        assert not fails

        # test dims
        dims = inference_data.posterior_predictive.dims["school"]
        pred_dims = inference_data.predictions.dims["school_pred"]
        assert dims == 8
        assert pred_dims == 8

    @pytest.mark.skipif(
        packaging.version.parse(pyro.__version__) < packaging.version.parse("1.0.0"),
        reason="requires pyro 1.0.0 or higher",
    )
    def test_inference_data_has_log_likelihood_and_observed_data(self, data):
        idata = from_pyro(data.obj)
        test_dict = {"log_likelihood": ["obs"], "observed_data": ["obs"]}
        fails = check_multiple_attrs(test_dict, idata)
        assert not fails

    def test_inference_data_no_posterior(
        self, data, eight_schools_params, predictions_data, predictions_params
    ):
        posterior_samples = data.obj.get_samples()
        model = data.obj.kernel.model
        posterior_predictive = Predictive(model, posterior_samples)(
            eight_schools_params["J"], torch.from_numpy(eight_schools_params["sigma"]).float()
        )
        prior = Predictive(model, num_samples=500)(
            eight_schools_params["J"], torch.from_numpy(eight_schools_params["sigma"]).float()
        )
        predictions = predictions_data
        constant_data = {"J": 8, "sigma": eight_schools_params["sigma"]}
        predictions_constant_data = predictions_params
        # only prior
        inference_data = from_pyro(prior=prior)
        test_dict = {"prior": ["mu", "tau", "eta"]}
        fails = check_multiple_attrs(test_dict, inference_data)
        assert not fails, "only prior: {}".format(fails)
        # only posterior_predictive
        inference_data = from_pyro(posterior_predictive=posterior_predictive)
        test_dict = {"posterior_predictive": ["obs"]}
        fails = check_multiple_attrs(test_dict, inference_data)
        assert not fails, "only posterior_predictive: {}".format(fails)
        # only predictions
        inference_data = from_pyro(predictions=predictions)
        test_dict = {"predictions": ["obs"]}
        fails = check_multiple_attrs(test_dict, inference_data)
        assert not fails, "only predictions: {}".format(fails)
        # only constant_data
        inference_data = from_pyro(constant_data=constant_data)
        test_dict = {"constant_data": ["J", "sigma"]}
        fails = check_multiple_attrs(test_dict, inference_data)
        assert not fails, "only constant_data: {}".format(fails)
        # only predictions_constant_data
        inference_data = from_pyro(predictions_constant_data=predictions_constant_data)
        test_dict = {"predictions_constant_data": ["J", "sigma"]}
        fails = check_multiple_attrs(test_dict, inference_data)
        assert not fails, "only predictions_constant_data: {}".format(fails)
        # prior and posterior_predictive
        idata = from_pyro(
            prior=prior,
            posterior_predictive=posterior_predictive,
            coords={"school": np.arange(eight_schools_params["J"])},
            dims={"theta": ["school"], "eta": ["school"]},
        )
        test_dict = {"posterior_predictive": ["obs"], "prior": ["mu", "tau", "eta", "obs"]}
        fails = check_multiple_attrs(test_dict, idata)
        assert not fails, "prior and posterior_predictive: {}".format(fails)

    def test_inference_data_only_posterior(self, data):
        idata = from_pyro(data.obj)
        test_dict = {"posterior": ["mu", "tau", "eta"], "sample_stats": ["diverging"]}
        fails = check_multiple_attrs(test_dict, idata)
        assert not fails

    @pytest.mark.skipif(
        packaging.version.parse(pyro.__version__) < packaging.version.parse("1.0.0"),
        reason="requires pyro 1.0.0 or higher",
    )
    def test_inference_data_only_posterior_has_log_likelihood(self, data):
        idata = from_pyro(data.obj)
        test_dict = {"log_likelihood": ["obs"]}
        fails = check_multiple_attrs(test_dict, idata)
        assert not fails

    def test_multiple_observed_rv(self):
        import pyro.distributions as dist
        from pyro.infer import MCMC, NUTS

        y1 = torch.randn(10)
        y2 = torch.randn(10)

        def model_example_multiple_obs(y1=None, y2=None):
            x = pyro.sample("x", dist.Normal(1, 3))
            pyro.sample("y1", dist.Normal(x, 1), obs=y1)
            pyro.sample("y2", dist.Normal(x, 1), obs=y2)

        nuts_kernel = NUTS(model_example_multiple_obs)
        mcmc = MCMC(nuts_kernel, num_samples=10)
        mcmc.run(y1=y1, y2=y2)
        inference_data = from_pyro(mcmc)
        test_dict = {
            "posterior": ["x"],
            "sample_stats": ["diverging"],
            "log_likelihood": ["y1", "y2"],
            "observed_data": ["y1", "y2"],
        }
        fails = check_multiple_attrs(test_dict, inference_data)
        assert not fails
        assert not hasattr(inference_data.sample_stats, "log_likelihood")

    def test_inference_data_constant_data(self):
        import pyro.distributions as dist
        from pyro.infer import MCMC, NUTS

        x1 = 10
        x2 = 12
        y1 = torch.randn(10)

        def model_constant_data(x, y1=None):
            _x = pyro.sample("x", dist.Normal(1, 3))
            pyro.sample("y1", dist.Normal(x * _x, 1), obs=y1)

        nuts_kernel = NUTS(model_constant_data)
        mcmc = MCMC(nuts_kernel, num_samples=10)
        mcmc.run(x=x1, y1=y1)
        posterior = mcmc.get_samples()
        posterior_predictive = Predictive(model_constant_data, posterior)(x1)
        predictions = Predictive(model_constant_data, posterior)(x2)
        inference_data = from_pyro(
            mcmc,
            posterior_predictive=posterior_predictive,
            predictions=predictions,
            constant_data={"x1": x1},
            predictions_constant_data={"x2": x2},
        )
        test_dict = {
            "posterior": ["x"],
            "posterior_predictive": ["y1"],
            "sample_stats": ["diverging"],
            "log_likelihood": ["y1"],
            "predictions": ["y1"],
            "observed_data": ["y1"],
            "constant_data": ["x1"],
            "predictions_constant_data": ["x2"],
        }
        fails = check_multiple_attrs(test_dict, inference_data)
        assert not fails

    def test_inference_data_num_chains(self, predictions_data, chains):
        predictions = predictions_data
        inference_data = from_pyro(predictions=predictions, num_chains=chains)
        nchains = inference_data.predictions.dims["chain"]
        assert nchains == chains