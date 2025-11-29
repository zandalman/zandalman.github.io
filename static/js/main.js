$(document).ready(function () {

    // Define places with their names and dates
    var places = [
        { id: "Evanston", name: "Evanston, IL", date: "2015 - 2019" },
        { id: "New-Haven", name: "New Haven, CT", date: "2019 - 2023" },
        { id: "Santa-Cruz", name: "Santa Cruz, CA", date: "2022 (summer)" },
        { id: "Los-Alamos", name: "Los Alamos, NM", date: "2024 (summer)" },
        { id: "Princeton", name: "Princeton, NJ", date: "2023 - 2028" }
    ];

    var placeIdx = 0;

    function showPlace(idx) {
        var place = places[idx];

        // Update dots
        $(".dot").removeClass("active");
        $("#" + place.id).addClass("active");

        // Update place info paragraphs
        $(".place-info").addClass("hidden");
        $("#" + place.id + "-info").removeClass("hidden");

        // Update nav
        $("#current-place").text(place.name);
        $("#current-date").text(place.date);
    }

    // Initial display
    showPlace(placeIdx);

    // Dot click
    $(".dot").on("click", function () {
        placeIdx = places.findIndex(p => p.id === $(this).attr("id"));
        showPlace(placeIdx);
    });

    // Next button
    $("#next").on("click", function () {
        placeIdx = (placeIdx + 1) % places.length;
        showPlace(placeIdx);
    });

    // Previous button
    $("#previous").on("click", function () {
        placeIdx = (placeIdx + places.length - 1) % places.length;
        showPlace(placeIdx);
    });

});
