const url = "https://swapi-api.hbtn.io/api/films/?format=json";

$.get(url, function (data) {
    const movie = data.results;
    for (films of movie)
        $("UL#list_movies").append("<li>" + films.title + "</li>");
});