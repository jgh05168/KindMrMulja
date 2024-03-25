// read-only
const payRouter = require("express").Router();

const controller = require("./payments.controller");

payRouter.route("/confirm").get(controller.confirmPayment);

module.exports = payRouter;
