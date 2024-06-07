 // Copyright (c) 2024, Nirmal Rathod and contributors
 // For license information, please see license.txt

 frappe.ui.form.on("Airline", {
 	refresh(frm) {
 		 let webSite = frm.doc.website;
 		 if (webSite) {
 			frm.add_web_link(webSite, "Visit Website");
 		 }
 	}
 });



//
// frappe.ui.form.on("Airline", {
//    // frm passed as the first parameter
//		founding_year(frm) {
//			console.log("Hello")
//		}
//	})
