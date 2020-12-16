let interval = 30
let time = 5000
let flag = 1
let t_int
$(document).ready(function () {
  let url, interval, flag
  csrf = $('input[name=csrfmiddlewaretoken]').val()
});

$(document).on('click', '.btn', function() {
  clearInterval(t_int)
  url = $(this)[0].name
  flag = 1
  $(this)[0].style.display = 'none'
  $(this)[0].parentNode.children[1].style.display ='block'
});

$(document).on('click', '.btn_up', function() {
  url = $(this)[0].name
  interval = $('input[name=interval]').val()
  flag = 2
  $(this)[0].style.display = 'none'
  $(this)[0].parentNode.children[0].style.display ='block'
});

$(document).on('click', '.interval_btn', function() {
  url = ''
  interval = $('input[name=interval]').val()
  time = interval * 1000
  flag = 1
});

$(document).ready(function () {
  setInterval( function () {
    $.ajax({
      type: 'post',
      url: "/ajax/",
      async: false,
      data: {
          csrfmiddlewaretoken: csrf,
          url: url,
          interval: interval,
          flag: flag,
      },
      success: function (data) {
      y = 0
      console.log(data)
      x = [...document.querySelectorAll('.status')]
      .map( item => {
        item.textContent = Object.values(data)[y]
        y ++
        // t_int = setInterval(ajax, time)
      })
    }});
  }, time);
  })
