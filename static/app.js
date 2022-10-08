
// ##############################
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

// ##############################
async function create_item(){
  const frm = event.target
  console.log(frm)
  const conn = await fetch('item', {
    method : "POST",
    body : new FormData(frm)
  })
  const item = await conn.json()
  if(!conn.ok){
    alert('Cannot create item')
    return
  }   
  console.log(item)
  document.querySelector("#items").insertAdjacentHTML('afterbegin', `
    <form autocomplete="off" class="item" onsubmit="delete_item(); return false">
      <input name="item_id" style="display: none;" type="text" value="${item.id}">
      <input name="item_name" oninput="update_item()" type="text" value="${item.name}">
      <input name="item_price" oninput="update_item()" type="text" value="${item.price}">
      <button class="simple_button">🗑️</button>
    </form> 
  `)   
  frm.reset()
  frm.querySelector("input").focus()
}

// ##############################
let timer = null
async function update_item(){
  const frm = event.target.form
  if(timer){clearTimeout(timer)}
    timer = setTimeout(async ()=>{
    console.log(frm)
    const conn = await fetch('item', {
      method : "PATCH",
      body : new FormData(frm)
    })
    const data = await conn.json()
    if(!conn.ok){
      alert('Cannot update item')
      return
    }  
    console.log("updated")         
  }, 1000)      
}
