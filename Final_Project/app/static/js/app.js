$(document).ready(function() {
    // Function to send message to AI and receive response
    function sendToAI(message) {
        $.ajax({
            url: '/ask_ai',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ message: message }),
            success: function(response) {
                // Display the AI's reply in the chatbox
                $('#chatbox-messages').append('<div><strong>AI:</strong> ' + response.reply + '</div>');

                // Update pizza order form with AI response
                if (response.order) {
                    // Set pizza size
                    $('select[name="size"]').val(response.order.size);

                    // Set toppings
                    $('input[name="toppings"]').each(function() {
                        if (response.order.toppings.includes($(this).val())) {
                            $(this).prop('checked', true);
                        } else {
                            $(this).prop('checked', false);
                        }
                    });

                    // Set quantity
                    $('input[name="quantity"]').val(response.order.quantity || 1);

                    // Set sauce
                    if (response.order.sauce) {
                        $('input[name="sauce"]').each(function() {
                            if ($(this).val() === response.order.sauce) {
                                $(this).prop('checked', true);  // Select the radio button for the sauce
                            } else {
                                $(this).prop('checked', false); // Deselect other sauce options
                            }
                        });
                    }
                }

                $('#chatbox-messages').scrollTop($('#chatbox-messages')[0].scrollHeight);
            },
            error: function() {
                $('#chatbox-messages').append('<div><strong>Error:</strong> Unable to process request.</div>');
            }
        });
    }

    // Handle sending message when the user presses the send button
    $('#send-button').click(function() {
        var userMessage = $('#user-input').val();
        if (userMessage.trim() !== '') {
            $('#chatbox-messages').append('<div><strong>You:</strong> ' + userMessage + '</div>');
            $('#user-input').val('');
            $('#chatbox-messages').scrollTop($('#chatbox-messages')[0].scrollHeight);

            sendToAI(userMessage); // Send message to AI
        }
    });

    // Optionally, handle pressing "Enter" key to send message
    $('#user-input').keypress(function(e) {
        if (e.which === 13) { // Enter key
            $('#send-button').click();
        }
    });
});
