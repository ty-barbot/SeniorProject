jQuery(document).ready(function () {

    $("body").on("click", ".view-workout", function (event) {
        console.log('TEST');
        let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
        let machine_type = jQuery(this).val();
        let machineViewUrl = JSON.parse(document.getElementById("machine_view_url").textContent);
        console.log(machine_type)
        jQuery.post(machineViewUrl, {
            machine_type: machine_type,
            csrfmiddlewaretoken: csrftoken
        }).done(function (data) {
                window.location.href = '/machines_view/'
            })
    });
});
