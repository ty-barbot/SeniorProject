jQuery(document).ready(function () {
    jQuery("#edit-profile").on("click", function () {
        jQuery(".profile-data-numbers").toggleClass("d-none");
        jQuery(".profile-data-input").toggleClass("d-none");
        if(jQuery("#edit-icon").hasClass("fa-edit"))
        {
            jQuery("#save-profile").toggleClass("d-none")
            jQuery("#edit-icon").addClass("fa-undo-alt")
            jQuery("#edit-icon").removeClass("fa-edit")
        }
        else{
            jQuery("#save-profile").toggleClass("d-none")
            jQuery("#edit-icon").addClass("fa-edit")
            jQuery("#edit-icon").removeClass("fa-undo-alt")
        }
    });

});
