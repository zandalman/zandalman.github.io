$(document).ready(function () {

    var placeIdx = 0;
    var places = [
        "Evanston",
        "New-Haven",
        "Santa-Cruz",
        "Princeton"
    ];

    $(".dot").on("click", function () {

        $(".dot").removeClass("active");
        $(this).addClass("active");

        placeInfoID = $(this).attr("id") + "-info";
        $(".place-info").addClass("hidden");
        $("#" + placeInfoID).removeClass("hidden");
    });

    $("#next").on("click", function () {
        placeIdx = (placeIdx + 1) % 4;
        placeId = places[placeIdx];
        $("#" + placeId).click();
    });

    $("#previous").on("click", function () {
        placeIdx = (placeIdx + 3) % 4;
        placeId = places[placeIdx];
        $("#" + placeId).click();
    });

});