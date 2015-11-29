//----------------------- biz logic -------------------------
var plot_data, query_data;
// send HQL to hive - string HQL input
function initialize() {
  var HQL = 'select distinct state from m_segment order by state';
  console.log('Start query states: ' + HQL)
  $.ajax({
    type: "GET",
    url: "http://" + host + ":8330/cgi-bin/HQL_SELECT.py",
    data: { hql: HQL }
  }).done(function(output) {
     // get return
     states = output;
     console.log('State HQL completed with ' + output.length + ' rows.');
     getCategories();
  });
}

function getCategories() {
  var HQL = 'select distinct category from m_segment where category in (0,1,2,3,4,5) order by category';
  console.log('Start query categories: ' + HQL)
  $.ajax({
    type: "GET",
    url: "http://" + host + ":8330/cgi-bin/HQL_SELECT.py",
    data: { hql: HQL }
  }).done(function(output) {
     // get return
     categories = output;
     console.log('Category HQL completed with ' + output.length + ' rows.');
     getCities();
  });
}

function getCities() {
  var HQL = "select distinct concat(city, ', ', state) as c from m_segment order by c";
  console.log('Start query cities: ' + HQL)
  $.ajax({
    type: "GET",
    url: "http://" + host + ":8330/cgi-bin/HQL_SELECT.py",
    data: { hql: HQL }
  }).done(function(output) {
     // get return
     cities = output;
     console.log('City HQL completed with ' + output.length + ' rows.');
     populateDropdowns()
  });
}

function populateDropdowns() {
  console.log('start refreshing dropdowns.')
  // clear first
  $('#state').empty();
  $('#city').empty();
  $('#category').empty();
  // populate
  $.each(states, function(i, v) {
    $('#state')
      .append($("<option></option>")
      .attr('value', v.row.trim())
      .text(v.row.trim()));
  });
  $.each(cities, function(i, v) {
    $('#city')
      .append($("<option></option>")
      .attr('value', v.row.trim())
      .text(v.row.trim()));
  });
  $.each(categories, function(i, v) {
    $('#category')
      .append($("<option></option>")
      .attr('value', v.row.trim())
      .text(v.row.trim()));
  });
  // refresh
  $('#state').selectmenu('refresh');
  $('#city').selectmenu('refresh');
  $('#category').selectmenu('refresh');
  console.log('dropdown refreshing components.')
}

function refreshData() {
  var HQL = "select seg.name, str.distance, str.altitude \
    from m_stream str join m_segment seg on str.seg_id = seg.id \
    where seg.state = '" + $('#state').val() + "' and seg.category = " + $('#category').val()
    + " order by name, distance";
  console.log('Start query stream altitude: ' + HQL)
  $.ajax({
    type: "GET",
    url: "http://" + host + ":8330/cgi-bin/HQL_SELECT.py",
    data: { hql: HQL }
  }).done(function(output) {
     // get return
     stream = output;
     console.log('Stream altitude HQL completed with ' + output.length + ' rows.');
     refreshChart();
  });
}

function refreshChart() {
  console.log('Start sorting data ...');
  var csvData = stream.map(function(r) {
    columns = r.row.split('|');
    return {
      segment: columns[0],
      distance: +columns[1],
      altitude: +columns[2]
    }
  });
  console.log('complete sorting data ...');
  plot_voronoi(csvData, 'dummy');
}
//----------------------- biz logic -------------------------
