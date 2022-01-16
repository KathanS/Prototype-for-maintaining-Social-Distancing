var express = require('express');
var router = express.Router();
let images = ["https://images.unsplash.com/photo-1604580824859-20d9665f58b5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60",
              "https://images.unsplash.com/photo-1603999870974-2cd2258dac8a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60",
              "https://images.unsplash.com/photo-1604502130010-22a9eb4c77a8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60",
              "https://images.unsplash.com/photo-1604180540768-78abbc4ab189?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60"]
let people = 12
/* GET home page. */
const today = new Date();
const time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Advance Computer Vision Project', images: images, people: people, time: time });
});

module.exports = router;
