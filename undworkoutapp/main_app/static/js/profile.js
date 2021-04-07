jQuery(document).ready(function () {
    jQuery("#edit-profile").on("click", function () {
        jQuery(".profile-data-numbers").toggleClass("d-none");
        jQuery(".profile-data-input").toggleClass("d-none");
        //now editing
        if (jQuery("#edit-icon").hasClass("fa-edit")) {
            jQuery("#save-profile").toggleClass("d-none");
            jQuery("#edit-icon").addClass("fa-undo-alt");
            jQuery("#edit-icon").removeClass("fa-edit");
        }
        //no longer editing
        else {
            jQuery("#save-profile").toggleClass("d-none");
            jQuery("#edit-profile-weight").val('');
            jQuery("#edit-profile-height").val('');
            jQuery("#edit-profile-age").val('');
            jQuery("#edit-icon").addClass("fa-edit");
            jQuery("#edit-icon").removeClass("fa-undo-alt");
        }
    });
    jQuery("#save-profile").on("click", function () {
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
        let EPuser = jQuery(this).data("user");
        let editProfileUrl = JSON.parse(document.getElementById("edit_profile_url").textContent);
        let new_weight = jQuery("#edit-profile-weight").val();
        let new_height = jQuery("#edit-profile-height").val();
        let new_birthdate = jQuery("#edit-profile-age").val();
        //let csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
        //xhr.setRequestHeader("X-CSRFToken", csrftoken);
        bootbox.confirm({
            title: "Please confirm details.",
            message: "Are you sure you want to save these changes?",
            callback: function (result) {
                if (result) jQuery.post(editProfileUrl, {
                    user_profile: EPuser,
                    new_weight: new_weight,
                    new_height: new_height,
                    new_birthdate: new_birthdate,
                    csrfmiddlewaretoken: csrftoken
                }).done(function (data) {
                    location.reload();
                })
            }

        });

        jQuery(".profile-data-numbers").toggleClass("d-none");
        jQuery(".profile-data-input").toggleClass("d-none");
        if (jQuery("#edit-icon").hasClass("fa-edit")) {
            jQuery("#save-profile").toggleClass("d-none");
            jQuery("#edit-icon").addClass("fa-undo-alt");
            jQuery("#edit-icon").removeClass("fa-edit");
        } else {
            jQuery("#save-profile").toggleClass("d-none");
            jQuery("#edit-icon").addClass("fa-edit");
            jQuery("#edit-icon").removeClass("fa-undo-alt");
        }
    });

});
