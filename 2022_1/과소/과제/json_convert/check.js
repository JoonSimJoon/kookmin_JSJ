var memberData = new Object();
memberData.name = "Derveljun";
memberData.activeFlg = true;
memberData.age = 20;

// Array에 담을 Item 객체를 만들어줍니다.
var pointHistoryItem1 = new Object();
pointHistoryItem1.useDate = 20200101;
pointHistoryItem1.usePoint = 1000;
pointHistoryItem1.accuralPoint = 100;
pointHistoryItem1.channel = "강남주점";

var pointHistoryItem2 = new Object();
pointHistoryItem2.useDate = 20200102;
pointHistoryItem2.usePoint = 0;
pointHistoryItem2.accuralPoint = 100;
pointHistoryItem2.channel = "강서마트";

// Item 객체를 Array에 담아줍니다.
var arrPointHistory = new Array();
arrPointHistory.push(pointHistoryItem1);
arrPointHistory.push(pointHistoryItem2);

// Array를 Object에 담아줍니다.
memberData.pointHistory = arrPointHistory;

console.log(memberData);

var jsonData = JSON.stringify(memberData);

console.log(jsonData);