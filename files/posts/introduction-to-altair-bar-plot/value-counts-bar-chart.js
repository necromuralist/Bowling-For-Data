
     (function(vegaEmbed) {
       var spec = {"$schema": "https://vega.github.io/schema/vega-lite/v5.6.1.json", "config": {"view": {"continuousHeight": 300, "continuousWidth": 300}}, "data": {"name": "data-774be733c0ac4b1e0a7bf95a840a22e6"}, "datasets": {"data-774be733c0ac4b1e0a7bf95a840a22e6": [{"count": 27, "year": 2005}, {"count": 89, "year": 2006}, {"count": 102, "year": 2007}, {"count": 110, "year": 2008}, {"count": 114, "year": 2009}, {"count": 124, "year": 2010}, {"count": 146, "year": 2011}, {"count": 141, "year": 2012}, {"count": 136, "year": 2013}, {"count": 144, "year": 2014}, {"count": 142, "year": 2015}, {"count": 141, "year": 2016}, {"count": 147, "year": 2017}, {"count": 141, "year": 2018}, {"count": 143, "year": 2019}, {"count": 116, "year": 2020}, {"count": 122, "year": 2021}, {"count": 114, "year": 2022}]}, "encoding": {"x": {"field": "year", "type": "nominal"}, "y": {"field": "count", "type": "quantitative"}}, "height": 600, "mark": {"type": "bar"}, "width": 800};

      var embedOpt = {"mode": "vega-lite"};

      function showError(el, error){
          el.innerHTML = ('<div class="error" style="color:red;">'
                          + '<p>JavaScript Error: ' + error.message + '</p>'
                          + "<p>This usually means there's a typo in your chart specification. "
                          + "See the javascript console for the full traceback.</p>"
                          + '</div>');
          throw error;
      } // showError
      const el = document.getElementById('value-counts-bar-chart-a897e2c7');
      vegaEmbed("#value-counts-bar-chart-a897e2c7", spec, embedOpt)
        .catch(error => showError(el, error));
    })(vegaEmbed);
