
var map;
var view;
var pivotalLoc;

function init(){
  pivotalloc = ol.proj.fromLonLat([-122.1478,37.3941]);

  viw = new ol.View({
    center: pivotalLoc,
    zoom: 6

  })

  map = new ol.Map({
    target:'map',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    loadTitlesWhileAnimating: true,
    view: view
  });
}
function panHome(){
  view.animate ({
    center:pivotalLoc,
    duration: 2000
  })
}
