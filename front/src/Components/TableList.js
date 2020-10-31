import React, { useState, useEffect } from "react";
import TableHead from "./TableHead";
import TableRow from "./TableRow";

const API_URL = "http://127.0.0.1:8000/api/";

const TableList = props => {
  const [list, setList] = useState([]);
  const [previous, setPrevious] = useState(null);
  const [next, setNext] = useState(null);
  const [url, setUrl] = useState(API_URL);

  useEffect(() => {
    fetch(url)
      .then(response => response.json())
      .then(obj => {
        setList(obj.results);
        setPrevious(obj.previous);
        setNext(obj.next);
      });
  }, [url]);

  const customers = list.map(customer => <TableRow key={customer.id} {...customer} />);

  return (
    <>
      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-around" }}>
        {previous && (
          <button onClick={() => setUrl(previous)} type="button" className="btn btn-primary mr-3">
            Previous
          </button>
        )}

        {next && (
          <button onClick={() => setUrl(next)} type="button" className="btn btn-primary">
            Next
          </button>
        )}
      </div>
      <table className="table table-dark mt-4">
        <TableHead />
        <tbody>{customers}</tbody>
      </table>
    </>
  );
};

export default TableList;
