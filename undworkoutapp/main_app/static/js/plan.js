jQuery(document).ready(function () {
    var $template = $(".template");
    var hash = 2;
    jQuery(".btn-add-panel").on("click", function () {
        var $newPanel = $template.clone();
        $newPanel.find(".collapse").removeClass("in");
        $newPanel.find(".toggle").attr("data-target", "#collapse" + (++hash))
            .text("Workout #" + hash);
        $newPanel.find(".collapse").attr("id", "collapse" + hash).attr("aria-labelledby", "heading" + hash);
        $newPanel.find(".card-header").attr("id", "heading" + hash);
        jQuery("#accordionExample").append($newPanel.fadeIn());
    });
    jQuery('.spinner-border').hide();
    console.log("here");
});
