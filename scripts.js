var created = false;

function buttonClick() {
  if (created) {
    window.scrollTo(0,0);
    location.href = "index.html"
  } else{
    var repetitions = document.getElementById("repetitions").value;
    var size = document.getElementById("sample_size").value;
    var data = parse_data(document.getElementById("data").value);
    var buckets = document.getElementById("buckets").value;
    var means = generate_means(size, data, repetitions);
    var dict = generate_axes(means, buckets)
    x = dict["x"];
    y = dict["y"];
    generate_graph(x,y);
    window.scrollTo(0,document.body.scrollHeight-100);
    created = true
    document.getElementById("button").value = "Start Over!"
  }
  return false;
}

function parse_data(str) {
  var i = str.length;
  var data = [];

  str = str.replace(/\D/g, ",");
  data = str.split(",");
  data = data.filter(function(entry) {
    return /\S/.test(entry);
  });

  return data;

}

function generate_means(sample_size, data, repetitions) {
  means = []

  while (means.length < repetitions) {
    var sum = 0
    for (i = 0; i < sample_size; i++) {
      sum += Number(data[Math.floor(Math.random() * data.length)]);
    }
    means[means.length] = sum / sample_size;
  }
  means = means.sort((a, b) => a - b);
  return means;
}

function generate_axes(means, buckets) {
  max_mean = Math.max(...means)
  min_mean = Math.min(...means)

  console.log(means)
  console.log(max_mean)
  console.log(min_mean)
  bucket_size = Math.ceil((max_mean - min_mean + 1) / buckets)
  console.log(bucket_size)
  bucket_number = 0;
  leftover_count = 0;

  x = [];
  y = [];

  i = 0;

  for (b = 0; b < buckets; b++) {
    start = b * bucket_size + min_mean;
    end = (b + 1) * bucket_size + min_mean;
    x[x.length] = start + "-" + end;
    y[y.length] = 0;

    while (i < means.length && means[i] < end) {
      y[b] = y[b] + 1;
      i = i + 1;
    }
  }

  return {
    "x": x,
    "y": y
  }
}

function generate_graph(x, y) {
  var ctx = document.getElementById('graph').getContext('2d');
  var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: x,
      datasets: [{
        label: 'Means',
        data: y,
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 1
      }]
    },
    options: {
      title: {
        display: true,
        text: "Frequency of Means"
      },
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true
          }
        }]
      }
    }
  });
  return myChart;
}
