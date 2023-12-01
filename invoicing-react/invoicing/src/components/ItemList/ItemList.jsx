export default function ItemList({ invoice, items }) {
  return (
    <>
      <h3 className="font-weight-bold mb-5">Invoice No. {invoice.invoice_id}</h3>
      <div className="container">
        <table className="table">
          <thead>
            <tr>
              <th scope="col">Item No</th>
              <th scope="col">Description</th>
              <th scope="col">Rate</th>
              <th scope="col">Quantity</th>
              <th scope="col">Total</th>
            </tr>
          </thead>
          <tbody>
            {items &&
              items.map((i, k) => (
                <tr>
                  <th>{k + 1}</th>
                  <td>{i.desc}</td>
                  <th>{i.rate}</th>
                  <td>{i.quantity}</td>
                  <td>{i.rate * i.quantity}</td>
                </tr>
              ))}
          </tbody>
        </table>
      </div>
    </>
  )
}
