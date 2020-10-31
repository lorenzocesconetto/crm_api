import React from "react";

const TableHead = props => {
  return (
    <thead>
      <tr>
        <th scope="col">id</th>
        <th scope="col">First name</th>
        <th scope="col">Last name</th>
        <th scope="col">Email</th>
        <th scope="col">Gender</th>
        <th scope="col">Company</th>
        <th scope="col">City</th>
        <th scope="col">Title</th>
        <th scope="col">Latitude</th>
        <th scope="col">Longitude</th>
      </tr>
    </thead>
  );
};

export default TableHead;
