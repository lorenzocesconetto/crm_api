import React from "react";

const TableRow = props => {
  return (
    <tr>
      <th scope="row">{props.id}</th>
      <td>{props.first_name}</td>
      <td>{props.last_name}</td>
      <td>{props.email}</td>
      <td>{props.gender}</td>
      <td>{props.company}</td>
      <td>{props.city}</td>
      <td>{props.title}</td>
      <td>{props.latitude}</td>
      <td>{props.longitude}</td>
    </tr>
  );
};

export default TableRow;
