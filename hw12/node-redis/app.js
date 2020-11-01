var redis = require('redis');

var client = redis.createClient(6379, "104.198.244.0");

client.on('connect', function() {
  console.log('connected');
  });

client.set('framework', 'AngularJS');
client.get('framework', function(err, reply) {
    console.log(reply);
});

client.hmset('frameworks', 'javascript', 'AngularJS', 'css', 'Bootstrap', 'node', 'Express');

client.hgetall('frameworks', function(err, object) {
    console.log(object);
});
