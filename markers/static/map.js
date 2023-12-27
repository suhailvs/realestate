const copy = "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a>";
const layer = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", { maxNativeZoom: 18, maxZoom: 20, attribution: copy, });
const map = L.map("map", { layers: [layer], });

map.locate()
  .on("locationfound", (e) => map.setView(e.latlng, 13))
  .on("locationerror", () => map.setView([10.59, 76.45], 13));

// We invoke this flow, every time the user stops moving on the map.
async function load_markers() {
  const markers_url = `/markers/api/markers/?in_bbox=${map.getBounds().toBBoxString()}`;
  const response = await fetch(markers_url);
  const geojson = await response.json();
  return geojson;
}

async function render_markers() {
  const markers = await load_markers();
  L.geoJSON(markers).bindPopup((layer) => layer.feature.properties.name).addTo(map);
}

map.on("moveend", render_markers);
