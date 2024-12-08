(function() {
    // Prevent multiple script executions
    if (window.emailFormInitialized) return;
    window.emailFormInitialized = true;

    document.addEventListener('DOMContentLoaded', function() {
        const form = document.getElementById('contactForm');
        const submitButton = form.querySelector('input[type="submit"]');
        const $submit = $('.submitting');

        // Singleton submission handler
        const emailSubmissionHandler = (function() {
            let isSubmitting = false;

            return function(e) {
                e.preventDefault();

                // Multiple layers of submission prevention
                if (isSubmitting) {
                    console.log('Submission already in progress');
                    return false;
                }

                // Validate inputs
                const senderEmail = document.getElementById('sender_email').value.trim();
                const appPassword = document.getElementById('app_password').value.trim();
                const receiverEmail = document.getElementById('receiver_email').value.trim();
                const subject = document.getElementById('subject').value.trim();
                const message = document.getElementById('message').value.trim();

                // Prevent immediate resubmission
                submitButton.disabled = true;
                isSubmitting = true;

                // Show submitting state
                $submit.css('display', 'block').text('Submitting...');

                // Clear previous messages
                $('#form-message-warning').hide();
                $('#form-message-success').hide();

                const emailData = {
                    email: senderEmail,
                    app_password: appPassword,
                    receiver_email: receiverEmail,
                    subject: subject,
                    message: message
                };

                // Remove existing listeners to prevent multiple submissions
                form.removeEventListener('submit', emailSubmissionHandler);

                fetch('http://127.0.0.1:5000/send-email', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(emailData),
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.success) {
                        // Clear any previous success/warning messages
                        $('#form-message-warning').hide();
                        
                        // Only show one success message
                        $('#form-message-success')
                            .html('Email sent successfully!')
                            .stop(true, true)  // Stop any ongoing animations
                            .fadeIn()
                            .delay(3000)
                            .fadeOut();

                        // Reset form
                        form.reset();
                    } else {
                        // Error handling
                        $('#form-message-warning')
                            .html(data.message || 'Failed to send email')
                            .fadeIn();
                    }
                })
                .catch(error => {
                    console.error("Error:", error);
                    $('#form-message-warning')
                        .html('Error sending email. Please try again.')
                        .fadeIn();
                })
                .finally(() => {
                    // Reset submission state
                    isSubmitting = false;
                    submitButton.disabled = false;
                    $submit.css('display', 'none');

                    // Re-add event listener
                    form.addEventListener('submit', emailSubmissionHandler);
                });

                return false;
            };
        })();

        // Initial event listener attachment
        form.addEventListener('submit', emailSubmissionHandler);
    });
})();