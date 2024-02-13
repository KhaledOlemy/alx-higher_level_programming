#!/usr/bin/node
let i;
exports.callMeMoby = function (x, theFunction) {
    for (i = 0; i < x; i++)
    {
	theFunction();
    }
};
