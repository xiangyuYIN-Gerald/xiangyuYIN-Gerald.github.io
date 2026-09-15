(function () {
  var status = document.getElementById('travel-status');
  if (!window.L) { status.textContent = 'Map library could not load. The visited countries are listed below.'; return; }
  var visited = {"GBR": ["United Kingdom", "英国"], "NOR": ["Norway", "挪威"], "SWE": ["Sweden", "瑞典"], "FRA": ["France", "法国"], "DEU": ["Germany", "德国"], "USA": ["United States", "美国"], "CHN": ["China", "中国（祖国）"], "AUT": ["Austria", "奥地利"], "BEL": ["Belgium", "比利时"], "ITA": ["Italy", "意大利"], "ESP": ["Spain", "西班牙"], "MLT": ["Malta", "马耳他"], "ARE": ["United Arab Emirates", "阿联酋"]};
  var map = L.map('travel-map', { scrollWheelZoom: false, minZoom: 1, maxZoom: 12, zoomSnap: 0.25 });
  function worldView() { map.fitBounds([[-58,-178],[80,178]], {padding:[8,8]}); }
  worldView();
  L.control.attribution({prefix:false}).addTo(map).addAttribution('Boundaries: <a href="https://www.naturalearthdata.com/">Natural Earth</a>');
  ['travel-world','travel-europe'].forEach(function(id) { document.getElementById(id).disabled = false; });
  document.getElementById('travel-world').onclick = worldView;
  document.getElementById('travel-europe').onclick = function () { map.fitBounds([[34,-12],[65,27]]); };
  function code(feature) { return feature.properties.ADM0_A3; }
  function isVisited(feature) { return !feature.properties.overseas && Boolean(visited[code(feature)]); }
  function style(feature) { return {color:'#ffffff', weight:0.7, fillColor:isVisited(feature) ? '#dc3545' : '#d2d8de', fillOpacity:1}; }
  var url = 'https://cdn.jsdelivr.net/gh/nvkelso/natural-earth-vector@v5.1.2/geojson/ne_50m_admin_0_countries.geojson';
  fetch(url).then(function(response) {
    if (!response.ok) throw new Error('Boundary download failed');
    return response.json();
  }).then(function(data) {
    // Separate distant polygons so overseas land remains visible but grey.
    var mainlandBoxes = {
      FRA: [[-6, 41, 10, 52]],
      NOR: [[4, 57, 32, 72]],
      USA: [[-126, 24, -66, 50], [-180, 51, -129, 72], [170, 51, 180, 72]],
      GBR: [[-9, 49, 2, 61]],
      ESP: [[-10, 35.9, 5, 44.5]],
      ITA: [[6, 35, 19, 48]]
    };
    var parts = [];
    data.features.forEach(function(feature) {
      var boxes = mainlandBoxes[code(feature)];
      if (!boxes || !feature.geometry || feature.geometry.type !== 'MultiPolygon') {
        parts.push(feature); return;
      }
      feature.geometry.coordinates.forEach(function(polygon) {
        var ring = polygon[0];
        var xs = ring.map(function(p) { return p[0]; });
        var ys = ring.map(function(p) { return p[1]; });
        var x = (Math.min.apply(null, xs) + Math.max.apply(null, xs)) / 2;
        var y = (Math.min.apply(null, ys) + Math.max.apply(null, ys)) / 2;
        var mainland = boxes.some(function(b) { return x >= b[0] && x <= b[2] && y >= b[1] && y <= b[3]; });
        parts.push({type:'Feature', properties:Object.assign({}, feature.properties, {overseas:!mainland}), geometry:{type:'Polygon', coordinates:polygon}});
      });
    });
    data.features = parts;
    var found = new Set(data.features.map(code));
    var missing = Object.keys(visited).filter(function(id) { return !found.has(id); });
    if (missing.length) throw new Error('Missing country boundaries: ' + missing.join(', '));
    var layer = L.geoJSON(data, {
      filter: function(feature) { return code(feature) !== 'ATA'; },
      style: style,
      onEachFeature: function(feature, polygon) {
        var names = isVisited(feature) ? visited[code(feature)] : null;
        var label = document.createElement('span');
        label.textContent = names ? names[0] + ' · ' + names[1] + ' — Visited' : (feature.properties.NAME_EN || feature.properties.NAME);
        if (feature.properties.overseas) label.textContent += ' — Overseas region';
        polygon.bindTooltip(label, {sticky:true});
        polygon.on('mouseover', function() { polygon.setStyle({weight:2, color:'#8d959d'}); });
        polygon.on('mouseout', function() { layer.resetStyle(polygon); });
        polygon.on('click', function() { map.fitBounds(polygon.getBounds(), {padding:[30,30], maxZoom:7}); });
      }
    }).addTo(map);
    status.textContent = 'Red countries are places I’ve visited. Hover for names, or select a country to zoom in.';

  }).catch(function() {
    status.textContent = 'Country boundaries could not load. Please check your connection and reload. All 13 visited countries are listed below.';
  });
}());
