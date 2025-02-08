class ButtonIos {
  constructor() {
    this.type = "ios"
  }
}
class ButtonPc {
  constructor() {
    this.type = "pc"
  }
}
class FactoryButton {
  createButton(os) {
    if(os === "ios") {
      return new ButtonIos()
    } else {
      return new ButtonPc()
    }
  }
}

let factory = new FactoryButton()
let button = factory.createButton("ios")
console.log(button.type)
