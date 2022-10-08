async function delete_item(){
  console.log(event.target)
  const frm = event.target
  const conn = await fetch("/item", {
    method: "DELETE",
    body: new FormData(frm)
  })
  const response = await conn.text()
  console.log(response)
  if(!conn.ok){
    alert("Upsss... cannot delete the item")
    return
  }
  frm.remove()
}