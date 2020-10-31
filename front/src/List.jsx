import React from "react";
import ReactDOM from "react-dom";
import TableList from "./Components/TableList";

window.renderApp = props =>
  ReactDOM.render(<TableList {...props} />, document.getElementById("react-container"));
