jQuery(document).ready(function () {
    var $template = $(".template");
    var hash = 1;
    jQuery(".btn-add-panel").on("click", function () {
        var $newPanel = $template.clone();
        $newPanel.find(".panel-heading").attr("id", "#plan-heading-" + (++hash));
        $newPanel.attr("id", "panel-plan-" + hash);
        $newPanel.find(".panel-collapse").attr("id", "plan-collapse-" + hash)
            .attr("aria-labelledby", "plan-heading-" + hash);
        $newPanel.find(".plan-heading-link").attr("href", "#plan-collapse-" + hash)
            .attr("aria-controls", "plan-collapse-" + hash); //.text("Exercise #" + hash);
        $newPanel.find(".exercise-name-input").val("").attr("placeholder", "Exercise #" + hash);
        $newPanel.find(".panel-set-info").attr("id", "#plan-collapse-" + hash);
        $newPanel.find(".btn-add-set").attr("id", "plan-collapse-" + hash);
        $newPanel.find(".remove-exercise-btn").attr("id", "panel-plan-" + hash);
        $newPanel.find(".panel-set-info").empty();
        jQuery("#accordion").append($newPanel.fadeIn());
    });
    var $setForm = $(".set-form");
    jQuery("body").on("click", ".btn-add-set", function (e) {
        var idClicked = e.target.id;
        var $newsetForm = $setForm.clone();
        $newsetForm = $newsetForm.removeClass("d-none");
        jQuery("#" + idClicked + " .panel-set-info").append($newsetForm.fadeIn());
    });
    $("body").on("click", ".remove-exercise-btn", function (event) {
        let panelID = $(this).attr("id");
        $(".panel-group").find("div#" + panelID).remove();
        console.log($(this).attr("id"));
    });
    $("body").on("click", "#save-workout-btn", function (event) {
        let workoutName = $("#workout-name").val();
        let workoutDate = $("#workout-date").val();
        let workoutCompleted = "True";
        if ($('#workout-completed').is(":checked")) {
            workoutCompleted = "True";
        }
        else
        {
            workoutCompleted = "False";
        }
        console.log(workoutCompleted);
        console.log("save");
    });

    jQuery('.spinner-border').hide();
});
