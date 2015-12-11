//----------------------- biz logic -------------------------
var plot_data, query_data;
// send HQL to hive - string HQL input
function initialize() {
  var HQL = 'select distinct state from m_segment order by state';
  console.log('Start querying states: ' + HQL)
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
  console.log('Start querying categories: ' + HQL)
  $.ajax({
    type: "GET",
    url: "http://" + host + ":8330/cgi-bin/HQL_SELECT.py",
    data: { hql: HQL }
  }).done(function(output) {
     // get return
     categories = output;
     console.log('Category HQL completed with ' + output.length + ' rows.');
     //getCities();
     getLeaderboard();
     populateDropdowns();
  });
}

function getCities() {
  var HQL = "select distinct concat(city, ', ', state) as c from m_segment order by c";
  console.log('Start querying cities: ' + HQL)
  $.ajax({
    type: "GET",
    url: "http://" + host + ":8330/cgi-bin/HQL_SELECT.py",
    data: { hql: HQL }
  }).done(function(output) {
     // get return
     cities = output;
     console.log('City HQL completed with ' + output.length + ' rows.');
     getLeaderboard();
     populateDropdowns()
  });
}

function populateDropdowns() {
  console.log('start refreshing dropdowns.')
  // clear first
  $('#state').empty();
  //$('#city').empty();
  $('#category').empty();
  // populate
  $.each(states, function(i, v) {
    $('#state')
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
  console.log('dropdown refreshing components.')
}

function refresh_data_hive() {
  var HQL = "select seg.name, str.distance, str.altitude, seg.id, seg.effort_count \
    from m_stream str join m_segment seg on str.seg_id = seg.id \
    where seg.state = '" + $('#state').val() + "' and seg.category = " + $('#category').val()
    + " order by name, distance";
  console.log('Start querying Hive stream altitude: ' + HQL)
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

function refresh_data_pg() {
  var SQL = "select seg.name, str.distance, str.altitude, seg.id, seg.effort_count \
    from stream str join segment seg on str.id = seg.id \
    where seg.state = '" + $('#state').val() + "' and seg.category = '" + $('#category').val()
    + "' order by name, distance";
  console.log('Start querying Postgres stream altitude: ' + SQL)
  $.ajax({
    type: "GET",
    url: "http://" + host + ":8330/cgi-bin/SQL_SELECT.py",
    data: { sql: SQL }
  }).done(function(output) {
     // get return
     stream = output;
     console.log('Stream altitude SQL completed with ' + output.length + ' rows.');
     if (output.length == 0) {
       alert('No category ' + $('#category').val() + ' segment found in ' + $('#state').val())
       return;
     }
     refreshChart();
  });
}

function getLeaderboard() {
  var HQL = 'select s.name, l.athlete_name, l.athlete_gender, l.moving_time, l.average_hr, l.rank \
    from m_leaderboard l join m_segment s on l.seg_id=s.id';
  console.log('Start querying leaderboard info: ' + HQL);
  $.ajax({
    type: "GET",
    url: "http://" + host + ":8330/cgi-bin/HQL_SELECT.py",
    data: { hql: HQL }
  }).done(function(output) {
     // get return
     leaderboard = output;
     console.log('Stream leaderboard HQL completed with ' + output.length + ' rows.');
     // get the js array to populate table
     leaderboard = leaderboard.map(function(r) { return r.row.split('|'); });
     table = $('#leaderboard').DataTable( {
             data: leaderboard,
             columns: [
                 { title: "Segment" },                 
                 { title: "Athlete" },
                 { title: "Gender" },
                 { title: "Time" },
                 { title: "Avg. Heartrate" },
                 { title: "Rank" }
             ]
      } );
      table.columns(0).search('!@#%$#%$$%#^%&^$&*').draw();
  });
}

function refreshChart() {
  if (stream.length == 0) {
    console.log('No data for the selected filter.');
    return;
  }
  console.log('Start sorting data ...');
  var csvData = stream.map(function(r) {
    columns = r.row.split('|');
    return {
      segment: columns[0],
      distance: +columns[1],
      altitude: +columns[2],
      seg_id: columns[3],
      cnt: columns[4]
    }
  });
  console.log('complete sorting data ...');
  // plot and populate table
  plot_voronoi(csvData, 'dummy');
}
//----------------------- biz logic -------------------------
