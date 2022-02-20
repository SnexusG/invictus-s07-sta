// $(function(){
//     var getListItem = function() {
//     	var items = listWidget.element().find(".dx-list-item");
//         var focusedItem = items.filter(".dx-state-focused").removeClass("dx-state-focused");
//         return focusedItem.length && focusedItem || items.first();
//     };
    
//     var listWidget = $("#list").dxList({
//         dataSource: products,
//         height: 400,
//         searchEnabled: true,
//         searchExpr: "Name",
//         searchEditorOptions: {
//             onInitialized: function(e) {
//                 var search = e.component;

//                 search.on("valueChanged", function() {
//                     clearTimeout(search.timeoutID);
//                     search.timeoutID = setTimeout(function() {
//                         getListItem().addClass("dx-state-focused");
//                     }); 
//                 });
                
//                 search.registerKeyHandler("upArrow", function() {
//                     getListItem().removeClass("dx-state-focused").prev().addClass("dx-state-focused");
//                 });
//                 search.registerKeyHandler("downArrow", function() {
//                     getListItem().removeClass("dx-state-focused").next().addClass("dx-state-focused");
//                 });
//             },
//             onDisposing: function(e) {
//                 clearTimeout(e.component.timeoutID);
//             }
//         },
//         itemTemplate: function(data) {
//             return $("<div>").text(data.Name);
//         }
//     }).dxList("instance");
// });

// var products = [{
//     "ID": 1,
//     "Name": "HD Video Player",
//     "Price": 330,
//     "Current_Inventory": 225,
//     "Backorder": 0,
//     "Manufacturing": 10,
//     "Category": "Video Players",
//     "ImageSrc": "https://js.devexpress.com/Demos/WidgetsGallery/JSDemos/images/products/1.png"
// }, {
//     "ID": 3,
//     "Name": "SuperPlasma 50",
//     "Price": 2400,
//     "Current_Inventory": 0,
//     "Backorder": 0,
//     "Manufacturing": 0,
//     "Category": "Televisions",
//     "ImageSrc": "https://js.devexpress.com/Demos/WidgetsGallery/JSDemos/images/products/3.png"
// }, {
//     "ID": 4,
//     "Name": "SuperLED 50",
//     "Price": 1600,
//     "Current_Inventory": 77,
//     "Backorder": 0,
//     "Manufacturing": 55,
//     "Category": "Televisions",
//     "ImageSrc": "https://js.devexpress.com/Demos/WidgetsGallery/JSDemos/images/products/4.png"
// }, ];