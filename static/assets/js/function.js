$(document).ready(function () {
    
    // Existing Contact Form AJAX Submission (No Changes)
    $(document).on("submit", "#contact-form-ajax", function (e) {
        e.preventDefault()
        console.log("Submited...");

        let full_name = $("#full_name").val()
        let email = $("#email").val()
        let phone = $("#phone").val()
        let subject = $("#subject").val()
        let message = $("#message").val()

        console.log("Name:", full_name);
        console.log("Email:", email);
        console.log("Phone:", phone);
        console.log("Subject:", subject);
        console.log("MEssage:", message);

        $.ajax({
            url: "/ajax-contact-form",
            data: {
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "subject": subject,
                "message": message,
            },
            dataType: "json",
            beforeSend: function () {
                console.log("Sending Data to Server...");
            },
            success: function (res) {
                console.log("Sent Data to server!");
                $(".contact_us_p").hide()
                $("#contact-form-ajax").hide()
                $("#message-response").html("Message sent successfully.")
            }
        })
    });

    // Existing Get Quote Form AJAX Submission (No Changes)
    $(document).on("submit", "#get-quote-ajax", function (e) {
        e.preventDefault()
        console.log("Submitted...");

        let email = $("#email-1").val()

        console.log("Email:", email);

        $.ajax({
            url: "/ajax-get-quote",
            data: {
                "email": email,
            },
            dataType: "json",
            beforeSend: function () {
                console.log("Sending Data to Server...");
            },
            success: function (res) {
                console.log("Sent Data to server!");
                $(".get_quote_hide").hide()
                $("#get-quote-ajax").hide()
                $("#confirmation").html("Will get back to you soon!")
            }
        })
    });

    // New Service Detail Page Form (Made Unique)
    $(document).on("submit", "#service-detail-form", function (e) {
        e.preventDefault(); // Prevent form submission
        console.log("Service Detail Form Submitted...");
    
        // Capture the correct page URL BEFORE making the AJAX request
        let servicePage = window.location.href; // Full URL
    
        console.log("Correct Page URL:", servicePage); // Ensure it's correct
    
        let serviceName = $("#service-name").val();
        let servicePhone = $("#service-phone").val();
        let serviceMessage = $("#service-message").val();
    
        $.ajax({
            url: "/ajax-service-detail-form/",
            type: "POST",
            data: {
                "name": serviceName,
                "phone": servicePhone,
                "message": serviceMessage,
                "page": servicePage, // Now sending the correct full page URL
                "csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]").val()
            },
            dataType: "json",
            beforeSend: function () {
                console.log("Sending Service Detail Data to Server...");
            },
            success: function (res) {
                console.log("Service Detail Data Sent to Server!");
    
                // Hide form and show success message
                $("#service-detail-form").hide();
                $("#service-response").html("Request submitted successfully!").show();
            }
        });
    });
});
