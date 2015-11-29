
function plot_voronoi(csv_data, price) {

  console.log(timestamp() + ': start plotting ...');
  $("body").css("cursor", "progress");
  var highlight_segment;

 var margin = {top: 20, right: 30, bottom: 30, left: 40},
  	width = 960 - margin.left - margin.right,
  	height = 500 - margin.top - margin.bottom;

  var x = d3.scale.linear().range([0, width]);
  //var x = d3.time.scale().range([0, width]);

  var y = d3.scale.linear().range([height, 0]);

  var voronoi = d3.geom.voronoi()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.value); })
    .clipExtent([[-margin.left, -margin.top], [width + margin.right, height + margin.bottom]]);

  var line = d3.svg.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.value); });

  // remove previous one then add
  d3.select('#voronoi').remove();
  svg = d3.select('body').append("svg").attr('id', 'voronoi')
   .attr("width", width + margin.left + margin.right)
   .attr("height", height + margin.top + margin.bottom)
   .append("g")
   .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  $('svg').on('click', function() {
    if (highlight_segment == null || highlight_segment == "") {
      console.log('no contract selected');
      return;
    }
    console.log(highlight_segment + ' is clicked!');
  });

  // bind data
  console.log(timestamp() + ': start converting data ...');
  cities = converter(csv_data, price);
  console.log(timestamp() + ': finish converting data ...');

  // get days
  var days = $(cities).map(function() { return this.values.map(function(r) { return r.date; }); });
  x.domain(d3.extent(days));
  y.domain([d3.min(cities, function(c) { return d3.min(c.values, function(d) { return d.value; }); }),
		    d3.max(cities, function(c) { return d3.max(c.values, function(d) { return d.value; }); })]).nice();

  svg.append("g")
      .attr("class", "axis axis--x")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.svg.axis()
        .scale(x)
        .orient("bottom"));

  svg.append("g")
      .attr("class", "axis axis--y")
      //.attr('transform', 'translate(30,0)')
      .call(d3.svg.axis()
        .scale(y)
        .orient("left"))
        //.ticks(10, "%"))
    .append("text")
      .attr("x", 4)
      .attr("dy", ".32em")
      .style("font-weight", "bold")
      .text("Altitude(m)");

  svg.append("g")
      .attr("class", "cities")
      .selectAll("path")
      .data(cities)
      .enter().append("path")
      .attr("d", function(d) { d.line = this; return line(d.values); });

  var focus = svg.append("g")
      .attr("transform", "translate(-100,-100)")
      .attr("class", "focus");

  focus.append("circle").attr("r", 3.5);

  focus.append("text").attr("y", -10);

  var voronoiGroup = svg.append("g").attr("class", "voronoi");

  console.log(timestamp() + ': start building voronoi mesh ...');
  voronoiGroup.selectAll("path")
      .data(voronoi(d3.nest()
          .key(function(d) { return x(d.date) + "," + y(d.value); })
          .rollup(function(v) { return v[0]; })
          .entries(d3.merge(cities.map(function(d) { return d.values; })))
          .map(function(d) { return d.values; }))
          //.filter(function(d) { return d != null; })
        )
    .enter().append("path")
      .attr("d", function(d) { return "M" + d.join("L") + "Z"; })
      .datum(function(d) { return d.point; })
      .on("mouseover", mouseover)
      .on("mouseout", mouseout);
  console.log(timestamp() + ': finish building voronoi mesh ...');
/*
  d3.select("#show-voronoi")
      .property("disabled", false)
      .on("change", function() { voronoiGroup.classed("voronoi--show", this.checked); });
*/
  function mouseover(d) {
    d3.select(d.city.line).classed("city--hover", true);
    d.city.line.parentNode.appendChild(d.city.line);
	highlight_segment = d.city.name;
    focus.attr("transform", "translate(" + x(d.date) + "," + y(d.value) + ")");
    focus.select("text").text(d.city.name);
  }

  function mouseout(d) {
    d3.select(d.city.line).classed("city--hover", false);
	highlight_segment = "";
    focus.attr("transform", "translate(-100,-100)");
  }
  $("body").css("cursor", "default");
  console.log(timestamp() + ': finish plotting');
}

function converter(csvData, field) {
  // get contracts
  var contracts = d3.set(csvData.map(function(row) { return row.segment; })).values();
  // for each contract, get one row of the weird data format
  rtn = contracts.map(function(contract) {
    var contract_rows = csvData.filter(function(row) {
      return row.segment == contract && row.distance != NaN && row.altitude != NaN; });
    var baseline = d3.min(contract_rows, function(d) { return d.altitude; });
	  var contract_data = {name: contract, values: null};
	  contract_data.values = contract_rows.map(function(row) {
	    return {
	      city: contract_data,
		    date: row.distance/1609.34, // in miles
		    value: row.altitude - baseline // price type
	    };
	  });

	  return contract_data;
  });
  return rtn;
}

function timestamp() {
  var dt = new Date();
  return dt.getHours() + ":" + dt.getMinutes() + ":" + dt.getSeconds();
}
