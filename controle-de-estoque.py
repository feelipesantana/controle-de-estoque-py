
products = []

def add_product():
    product = input("Digite o nome do produto: ");
    
    value = input("Digite o valor do produto: ");
    if value.isnumeric() == False:
      print("O valor do produto deve ser um número.");
      return;
    
    quantity = input("Digite a quantidade do produto: ");
    if quantity.isnumeric() == False:
        print("A quantidade do produto deve ser um número.");
        return;
    
    new_product = {
      "name": product,
      "value": float(value),
      "quantity": float(quantity)
    };
    products.append(new_product);
    
def update_product():
    item = input("Digite o nome do produto que deseja atualizar? ");
    new_price = input("Digite o novo preço do produto (ou deixe em branco para não alterar): ");
    new_quantity = input("Digite a nova quantidade do produto (ou deixe em branco para não alterar): ");
    
    for product in products:
      
      if product['name'] == item:
        if new_price.strip():
          new_price = float(new_price);
          product['value'] = new_price;
        
        if new_quantity.strip():
            new_quantity = float(new_quantity);
            product['quantity'] = new_quantity;
            print(f"Produto '{item}' atualizado com sucesso.");
            return;
      
  
def view_stock():
    for product in products:
      print(f"Nome: {product['name']}, Preço: R${product['value']:.2f}, Quantidade: {product['quantity']}")

def sair_do_sistema():
    print("Thauzinho !!! Feito por @felipesantanajs");
    return True

def main():
  sair = False;
  while not sair:
    print("\nMenu Princial:") 
    print("1. Adicionar produto")
    print("2. Atualizar produto")
    print("3. Visualizar estoque")
    print("4. Sair do sistema")
    
    option = input("Escolha uma opção: ");
    
    if option == "1":
      add_product()
    elif option == "2":
      update_product()
    elif option == "3":
      view_stock()
    elif option == "4":
      sair = sair_do_sistema();

if __name__ == "__main__":
    main()