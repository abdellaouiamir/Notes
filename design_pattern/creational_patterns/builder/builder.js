class Car {
  constructor() {
    this.marque = null
    this.color = null
    this.place = null
  }
  show_details() {
    return `${this.marque} . ${this.color} . ${this.place} .`
  }
}
class CarBuilder {
  constructor() {
    this.car = new Car()
  }
  addMarque(marque) {
    this.car.marque = marque
    return this
  }
  addColor(color) {
    this.car.color = color
    return this
  }
  addPlace(place) {
    this.car.place = place
    return this
  }
  build() {
    return this.car
  }
}

let carBuilder = new CarBuilder()
let car = carBuilder.addColor("red").addPlace(3).addMarque("audi").build()
console.log(car.show_details())

