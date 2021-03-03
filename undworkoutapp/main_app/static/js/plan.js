jQuery(document).ready(function () {
    var $template = $(".template");
    var hash = 1;
    jQuery(".btn-add-panel").on("click", function () {
        var $newPanel = $template.clone();
        $newPanel.find(".panel-heading").attr("id", "#plan-heading-" + (++hash));
        $newPanel.find(".panel-collapse").attr("id", "plan-collapse-" + hash).attr("aria-labelledby", "plan-heading-" + hash);
        $newPanel.find(".plan-heading-link").attr("href", "#plan-collapse-" + hash).attr("aria-controls", "plan-collapse-" + hash).text("Exercise #" + hash);
        $newPanel.find(".panel-set-info").attr("id", "#plan-collapse-" + hash);
        $newPanel.find(".btn-add-set").attr("id", "plan-collapse-" + hash);
        $newPanel.find(".panel-set-info").empty();
        jQuery("#accordion").append($newPanel.fadeIn());
    });
    var $setForm = $(".set-form");
    jQuery("body").on("click", ".btn-add-set", function (e) {
        var idClicked = e.target.id;
        var $newsetForm = $setForm.clone();
        jQuery("#"+idClicked + " .panel-set-info").append($newsetForm.fadeIn());
    });


    jQuery('.spinner-border').hide();
});
