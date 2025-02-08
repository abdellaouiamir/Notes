class Db_pool {
  static instance = null
  status = "disconnected"
  constructor() {
    this.status = "connected"
  }
  static create_connection() {
    if(instance === null) {
      instance = new Db_pool()
    }
    return this.instance
  }
}
