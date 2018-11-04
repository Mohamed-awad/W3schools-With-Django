$(function () {
  'use strict';
  $('.t1').click(function () {
    $('.ref').hide();
    $('.ex').hide();
    $('.tut1').toggle();
  });
  $('.r1').click(function () {
    $('.tut1').hide();
    $('.ex').hide();
    $('.ref').toggle();
  });
  $('.e1').click(function () {
    $('.ref').hide();
    $('.tut1').hide();
    $('.ex').toggle();
  });
});
