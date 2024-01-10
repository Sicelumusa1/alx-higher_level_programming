$(function() {
  $('#add_item').click(function() {
    const newTag = $('<li>Item</li>');
    $('ul.my_list')append(newTag);
  });
});
