// Copyright (c) 2024, Nirmal Rathod and contributors
// For license information, please see license.txt


frappe.ui.form.on("Airplane Ticket", {
  refresh: function(frm) {
    frm.add_custom_button(
      __("Assign Seat"),
      function () {
        frm.trigger("assign_seat");
      },
      __("Actions")
    );
  },


//  assign_seat: function(frm) {
//  var d = new frappe.ui.Dialog({
//  			//frappe.show_alert("Hello");
//
//
//
//  });
////    var number = Math.floor(Math.random() * 99) + 1;
////    // Generate a random uppercase letter using String.fromCharCode
////    var letter = String.fromCharCode(65 + Math.floor(Math.random() * 26));
////    // Combine number and letter to form seat assignment
////    var seat = number + letter;
//
//	//frm.set_value("seat", seat);
//
//  }

//assign_seat: function(frm) {
//  // Create a new instance of the frappe.ui.Dialog class
//  var d = new frappe.ui.Dialog({
//    title: 'Enter Seat Assignment', // Title of the dialog
//    fields: [
//      {
//        label: 'Seat Assignment',    // Label for the input field
//        fieldname: 'seat_assignment', // Field name for the input
//        fieldtype: 'Data',            // Type of the field (Data input)
//        reqd: 1                       // Make this field required
//      }
//    ],
//    primary_action_label: 'Submit',  // Label for the submit button
//    primary_action: function() {     // Action to take when the submit button is clicked
//      let data = d.get_values();     // Retrieve the values entered in the dialog
//      if (data) {
//        frappe.msgprint(`Seat Assignment: ${data.seat_assignment}`); // Display a message with the entered value
//        frm.set_value("seat", data.seat_assignment); // Set the 'seat' field in the form with the entered value
//        d.hide(); // Hide the dialog after submission
//      }
//    }
//  });
//
//  // Add a Cancel button
//  d.set_secondary_action(function() {
//    d.hide(); // Hide the dialog when Cancel is clicked
//  });
//
//  d.set_secondary_action_label('Cancel');
//
//  d.show(); // Show the dialog to the user
//}




//assign_seat: function(frm) {
//  var d = new frappe.ui.Dialog({
//    title: 'Enter Seat Assignment',
//    fields: [
//      {
//        label: 'Seat Assignment',
//        fieldname: 'seat_assignment',
//        fieldtype: 'Data',
//        reqd: 1
//      }
//    ],
//    primary_action_label: 'Submit',
//    primary_action: function() {
//      let data = d.get_values();
//      if (data) {
//        frappe.msgprint(`Seat Assignment: ${data.seat_assignment}`);
//        frm.set_value("seat", data.seat_assignment);
//        d.hide();
//      }
//    }
//  });
//
//  d.show();
//}

   //Function to generate and set a random seat assignment
auto_assign_seat:  function(frm) {
        var number = Math.floor(Math.random() * 99) + 1;
        var letter = String.fromCharCode(65 + Math.floor(Math.random() * 26));
        var seat = number + letter;
        frm.set_value("seat", seat);
        frappe.msgprint(`Automatically Assigned Seat: ${seat}`);
    },

assign_seat: function(frm) {


    // Create a new instance of the frappe.ui.Dialog class
    var d = new frappe.ui.Dialog({
        title: 'Enter Seat Assignment', // Title of the dialog
        fields: [
            {
                label: 'Seat Assignment',    // Label for the input field
                fieldname: 'seat_assignment', // Field name for the input
                fieldtype: 'Data',            // Type of the field (Data input)
                reqd: 1                       // Make this field required
            }
        ],

        primary_action_label: 'Submit',  // Label for the submit button
        primary_action: function() {     // Action to take when the submit button is clicked
            let data = d.get_values();     // Retrieve the values entered in the dialog
            if (data) {
                frappe.msgprint(`Seat Assignment: ${data.seat_assignment}`); // Display a message with the entered value
                frm.set_value("seat", data.seat_assignment); // Set the 'seat' field in the form with the entered value
                d.hide(); // Hide the dialog after submission
            }
        }

    });

    // Add a Cancel button
    d.set_secondary_action(function() {
        d.hide(); // Hide the dialog when Cancel is clicked
    });
    d.set_secondary_action_label('Cancel');
    d.show(); // Show the dialog to the user

   }




});
