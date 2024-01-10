$(function() {
  $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
    const movieTitles = data.results.map(movie => movie.title);

    for (const title of movieTitles) {
      $("ul#list_movies").append("<li>" + title + "</li>");
    }
  });
});
