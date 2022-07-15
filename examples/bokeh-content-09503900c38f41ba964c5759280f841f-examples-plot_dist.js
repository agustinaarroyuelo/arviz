(function() {
  const fn = function() {
    (function(root) {
      function now() {
        return new Date();
      }
    
      const force = false;
    
      if (typeof root._bokeh_onload_callbacks === "undefined" || force === true) {
        root._bokeh_onload_callbacks = [];
        root._bokeh_is_loading = undefined;
      }
    
    
    const element = document.getElementById("53b3aecc-9998-4809-9937-67f292859145");
        if (element == null) {
          console.warn("Bokeh: autoload.js configured with elementid '53b3aecc-9998-4809-9937-67f292859145' but no matching script tag was found.")
        }
      function run_callbacks() {
        try {
          root._bokeh_onload_callbacks.forEach(function(callback) {
            if (callback != null)
              callback();
          });
        } finally {
          delete root._bokeh_onload_callbacks
        }
        console.debug("Bokeh: all callbacks have finished");
      }
    
      function load_libs(css_urls, js_urls, callback) {
        if (css_urls == null) css_urls = [];
        if (js_urls == null) js_urls = [];
    
        root._bokeh_onload_callbacks.push(callback);
        if (root._bokeh_is_loading > 0) {
          console.debug("Bokeh: BokehJS is being loaded, scheduling callback at", now());
          return null;
        }
        if (js_urls == null || js_urls.length === 0) {
          run_callbacks();
          return null;
        }
        console.debug("Bokeh: BokehJS not loaded, scheduling load and callback at", now());
        root._bokeh_is_loading = css_urls.length + js_urls.length;
    
        function on_load() {
          root._bokeh_is_loading--;
          if (root._bokeh_is_loading === 0) {
            console.debug("Bokeh: all BokehJS libraries/stylesheets loaded");
            run_callbacks()
          }
        }
    
        function on_error(url) {
          console.error("failed to load " + url);
        }
    
        for (let i = 0; i < css_urls.length; i++) {
          const url = css_urls[i];
          const element = document.createElement("link");
          element.onload = on_load;
          element.onerror = on_error.bind(null, url);
          element.rel = "stylesheet";
          element.type = "text/css";
          element.href = url;
          console.debug("Bokeh: injecting link tag for BokehJS stylesheet: ", url);
          document.body.appendChild(element);
        }
    
        for (let i = 0; i < js_urls.length; i++) {
          const url = js_urls[i];
          const element = document.createElement('script');
          element.onload = on_load;
          element.onerror = on_error.bind(null, url);
          element.async = false;
          element.src = url;
          console.debug("Bokeh: injecting script tag for BokehJS library: ", url);
          document.head.appendChild(element);
        }
      };
    
      function inject_raw_css(css) {
        const element = document.createElement("style");
        element.appendChild(document.createTextNode(css));
        document.body.appendChild(element);
      }
    
      const js_urls = ["https://cdn.bokeh.org/bokeh/release/bokeh-2.4.3.min.js", "https://cdn.bokeh.org/bokeh/release/bokeh-gl-2.4.3.min.js", "https://cdn.bokeh.org/bokeh/release/bokeh-widgets-2.4.3.min.js", "https://cdn.bokeh.org/bokeh/release/bokeh-tables-2.4.3.min.js", "https://cdn.bokeh.org/bokeh/release/bokeh-mathjax-2.4.3.min.js"];
      const css_urls = [];
    
      const inline_js = [    function(Bokeh) {
          Bokeh.set_log_level("info");
        },
        function(Bokeh) {
          (function() {
            const fn = function() {
              Bokeh.safely(function() {
                (function(root) {
                  function embed_document(root) {
                  const docs_json = '{"30430fa4-9003-4dd5-9fb3-fc4256e51215":{"defs":[],"roots":{"references":[{"attributes":{"coordinates":null,"formatter":{"id":"20416"},"group":null,"major_label_policy":{"id":"20417"},"ticker":{"id":"20359"}},"id":"20358","type":"LinearAxis"},{"attributes":{},"id":"20421","type":"UnionRenderers"},{"attributes":{"coordinates":null,"formatter":{"id":"20419"},"group":null,"major_label_policy":{"id":"20420"},"ticker":{"id":"20355"}},"id":"20354","type":"LinearAxis"},{"attributes":{},"id":"20350","type":"LinearScale"},{"attributes":{"axis":{"id":"20354"},"coordinates":null,"group":null,"ticker":null},"id":"20357","type":"Grid"},{"attributes":{},"id":"20416","type":"BasicTickFormatter"},{"attributes":{"bottom_units":"screen","coordinates":null,"fill_alpha":0.5,"fill_color":"lightgrey","group":null,"left_units":"screen","level":"overlay","line_alpha":1.0,"line_color":"black","line_dash":[4,4],"line_width":2,"right_units":"screen","syncable":false,"top_units":"screen"},"id":"20399","type":"BoxAnnotation"},{"attributes":{"axis":{"id":"20358"},"coordinates":null,"dimension":1,"group":null,"ticker":null},"id":"20361","type":"Grid"},{"attributes":{},"id":"20419","type":"BasicTickFormatter"},{"attributes":{},"id":"20348","type":"DataRange1d"},{"attributes":{},"id":"20362","type":"PanTool"},{"attributes":{"below":[{"id":"20354"}],"center":[{"id":"20357"},{"id":"20361"},{"id":"20424"}],"height":500,"left":[{"id":"20358"}],"output_backend":"webgl","renderers":[{"id":"20411"}],"title":{"id":"20413"},"toolbar":{"id":"20369"},"width":500,"x_range":{"id":"20346"},"x_scale":{"id":"20350"},"y_range":{"id":"20348"},"y_scale":{"id":"20352"}},"id":"20345","subtype":"Figure","type":"Plot"},{"attributes":{"coordinates":null,"formatter":{"id":"20438"},"group":null,"major_label_policy":{"id":"20439"},"ticker":{"id":"20386"}},"id":"20385","type":"LinearAxis"},{"attributes":{},"id":"20394","type":"WheelZoomTool"},{"attributes":{"coordinates":null,"group":null},"id":"20432","type":"Title"},{"attributes":{},"id":"20386","type":"BasicTicker"},{"attributes":{"coordinates":null,"formatter":{"id":"20435"},"group":null,"major_label_policy":{"id":"20436"},"ticker":{"id":"20390"}},"id":"20389","type":"LinearAxis"},{"attributes":{},"id":"20393","type":"PanTool"},{"attributes":{"bottom":{"value":0},"fill_alpha":{"value":0.1},"fill_color":{"value":"#000000"},"hatch_alpha":{"value":0.1},"left":{"field":"left"},"line_alpha":{"value":0.1},"line_color":{"value":"#000000"},"right":{"field":"right"},"top":{"field":"top"}},"id":"20409","type":"Quad"},{"attributes":{},"id":"20359","type":"BasicTicker"},{"attributes":{"coordinates":null,"data_source":{"id":"20426"},"glyph":{"id":"20427"},"group":null,"hover_glyph":null,"muted_glyph":{"id":"20429"},"nonselection_glyph":{"id":"20428"},"view":{"id":"20431"}},"id":"20430","type":"GlyphRenderer"},{"attributes":{},"id":"20398","type":"HelpTool"},{"attributes":{},"id":"20381","type":"LinearScale"},{"attributes":{"bottom":{"value":0},"fill_color":{"value":"#000000"},"left":{"field":"left"},"line_alpha":{"value":0},"line_color":{"value":"#000000"},"right":{"field":"right"},"top":{"field":"top"}},"id":"20408","type":"Quad"},{"attributes":{"overlay":{"id":"20399"}},"id":"20395","type":"BoxZoomTool"},{"attributes":{},"id":"20439","type":"AllLabels"},{"attributes":{},"id":"20367","type":"HelpTool"},{"attributes":{"below":[{"id":"20385"}],"center":[{"id":"20388"},{"id":"20392"},{"id":"20443"}],"height":500,"left":[{"id":"20389"}],"output_backend":"webgl","renderers":[{"id":"20430"}],"title":{"id":"20432"},"toolbar":{"id":"20400"},"width":500,"x_range":{"id":"20377"},"x_scale":{"id":"20381"},"y_range":{"id":"20379"},"y_scale":{"id":"20383"}},"id":"20376","subtype":"Figure","type":"Plot"},{"attributes":{},"id":"20390","type":"BasicTicker"},{"attributes":{},"id":"20435","type":"BasicTickFormatter"},{"attributes":{},"id":"20365","type":"SaveTool"},{"attributes":{"line_color":"#ff0000","x":{"field":"x"},"y":{"field":"y"}},"id":"20427","type":"Line"},{"attributes":{},"id":"20366","type":"ResetTool"},{"attributes":{},"id":"20396","type":"SaveTool"},{"attributes":{"coordinates":null,"group":null,"items":[{"id":"20444"}]},"id":"20443","type":"Legend"},{"attributes":{},"id":"20377","type":"DataRange1d"},{"attributes":{},"id":"20440","type":"UnionRenderers"},{"attributes":{"overlay":{"id":"20368"}},"id":"20364","type":"BoxZoomTool"},{"attributes":{},"id":"20420","type":"AllLabels"},{"attributes":{"children":[{"id":"20345"},{"id":"20376"}]},"id":"20445","type":"Row"},{"attributes":{"tools":[{"id":"20362"},{"id":"20363"},{"id":"20364"},{"id":"20365"},{"id":"20366"},{"id":"20367"}]},"id":"20369","type":"Toolbar"},{"attributes":{"bottom_units":"screen","coordinates":null,"fill_alpha":0.5,"fill_color":"lightgrey","group":null,"left_units":"screen","level":"overlay","line_alpha":1.0,"line_color":"black","line_dash":[4,4],"line_width":2,"right_units":"screen","syncable":false,"top_units":"screen"},"id":"20368","type":"BoxAnnotation"},{"attributes":{},"id":"20441","type":"Selection"},{"attributes":{"source":{"id":"20407"}},"id":"20412","type":"CDSView"},{"attributes":{},"id":"20352","type":"LinearScale"},{"attributes":{},"id":"20363","type":"WheelZoomTool"},{"attributes":{"tools":[{"id":"20393"},{"id":"20394"},{"id":"20395"},{"id":"20396"},{"id":"20397"},{"id":"20398"}]},"id":"20400","type":"Toolbar"},{"attributes":{"axis":{"id":"20389"},"coordinates":null,"dimension":1,"group":null,"ticker":null},"id":"20392","type":"Grid"},{"attributes":{"line_alpha":0.1,"line_color":"#ff0000","x":{"field":"x"},"y":{"field":"y"}},"id":"20428","type":"Line"},{"attributes":{"bottom":{"value":0},"fill_alpha":{"value":0.2},"fill_color":{"value":"#000000"},"hatch_alpha":{"value":0.2},"left":{"field":"left"},"line_alpha":{"value":0.2},"line_color":{"value":"#000000"},"right":{"field":"right"},"top":{"field":"top"}},"id":"20410","type":"Quad"},{"attributes":{},"id":"20417","type":"AllLabels"},{"attributes":{"axis":{"id":"20385"},"coordinates":null,"group":null,"ticker":null},"id":"20388","type":"Grid"},{"attributes":{},"id":"20355","type":"BasicTicker"},{"attributes":{},"id":"20397","type":"ResetTool"},{"attributes":{"coordinates":null,"group":null},"id":"20413","type":"Title"},{"attributes":{"coordinates":null,"group":null,"items":[{"id":"20425"}]},"id":"20424","type":"Legend"},{"attributes":{},"id":"20346","type":"DataRange1d"},{"attributes":{"source":{"id":"20426"}},"id":"20431","type":"CDSView"},{"attributes":{},"id":"20383","type":"LinearScale"},{"attributes":{"label":{"value":"Gaussian"},"renderers":[{"id":"20430"}]},"id":"20444","type":"LegendItem"},{"attributes":{"data":{"left":[0,1,2,3,4,5,6,7,8,9,10,11,12],"right":[1,2,3,4,5,6,7,8,9,10,11,12,13],"top":{"__ndarray__":"WmQ730+Nlz9oke18PzWuPyPb+X5qvMQ/7nw/NV66yT+e76fGSzfJPzvfT42XbsI/MQisHFpkuz9YObTIdr6vP1g5tMh2vp8//Knx0k1igD97FK5H4Xp0PwAAAAAAAAAA/Knx0k1iUD8=","dtype":"float64","order":"little","shape":[13]}},"selected":{"id":"20422"},"selection_policy":{"id":"20421"}},"id":"20407","type":"ColumnDataSource"},{"attributes":{"label":{"value":"Poisson"},"renderers":[{"id":"20411"}]},"id":"20425","type":"LegendItem"},{"attributes":{},"id":"20438","type":"BasicTickFormatter"},{"attributes":{"data":{"x":{"__ndarray__":"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","dtype":"float64","order":"little","shape":[512]},"y":{"__ndarray__":"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","dtype":"float64","order":"little","shape":[512]}},"selected":{"id":"20441"},"selection_policy":{"id":"20440"}},"id":"20426","type":"ColumnDataSource"},{"attributes":{"coordinates":null,"data_source":{"id":"20407"},"glyph":{"id":"20408"},"group":null,"hover_glyph":null,"muted_glyph":{"id":"20410"},"nonselection_glyph":{"id":"20409"},"view":{"id":"20412"}},"id":"20411","type":"GlyphRenderer"},{"attributes":{},"id":"20379","type":"DataRange1d"},{"attributes":{},"id":"20436","type":"AllLabels"},{"attributes":{"line_alpha":0.2,"line_color":"#ff0000","x":{"field":"x"},"y":{"field":"y"}},"id":"20429","type":"Line"},{"attributes":{},"id":"20422","type":"Selection"}],"root_ids":["20445"]},"title":"Bokeh Application","version":"2.4.3"}}';
                  const render_items = [{"docid":"30430fa4-9003-4dd5-9fb3-fc4256e51215","root_ids":["20445"],"roots":{"20445":"53b3aecc-9998-4809-9937-67f292859145"}}];
                  root.Bokeh.embed.embed_items(docs_json, render_items);
                  }
                  if (root.Bokeh !== undefined) {
                    embed_document(root);
                  } else {
                    let attempts = 0;
                    const timer = setInterval(function(root) {
                      if (root.Bokeh !== undefined) {
                        clearInterval(timer);
                        embed_document(root);
                      } else {
                        attempts++;
                        if (attempts > 100) {
                          clearInterval(timer);
                          console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing");
                        }
                      }
                    }, 10, root)
                  }
                })(window);
              });
            };
            if (document.readyState != "loading") fn();
            else document.addEventListener("DOMContentLoaded", fn);
          })();
        },
    function(Bokeh) {
        }
      ];
    
      function run_inline_js() {
        for (let i = 0; i < inline_js.length; i++) {
          inline_js[i].call(root, root.Bokeh);
        }
      }
    
      if (root._bokeh_is_loading === 0) {
        console.debug("Bokeh: BokehJS loaded, going straight to plotting");
        run_inline_js();
      } else {
        load_libs(css_urls, js_urls, function() {
          console.debug("Bokeh: BokehJS plotting callback run at", now());
          run_inline_js();
        });
      }
    }(window));
  };
  if (document.readyState != "loading") fn();
  else document.addEventListener("DOMContentLoaded", fn);
})();