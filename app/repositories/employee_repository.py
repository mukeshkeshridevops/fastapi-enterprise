class EmployeeRepository:
    def get_all(self,db):
        return db.query(None)
