from auth.dao.packages_dao import PackagesDAO  
from flask import jsonify

class PackagesService:
    @staticmethod
    def get_all_packages():
        try:
            packages = PackagesDAO.get_all()
            return packages
        except Exception as e:
            raise Exception(f"Error retrieving packages: {str(e)}")

    @staticmethod
    def get_package_by_id(package_id: int):
        """Отримання пакунка за ID."""
        try:
            package = PackagesDAO.get_by_id(package_id)
            if not package:
                raise ValueError("Package not found.")
            return package
        except Exception as e:
            raise Exception(f"Error retrieving package: {str(e)}")
        
    @staticmethod
    def add_package(sender_id, receiver_id, delivery_address_id, description, status):
    
        if not sender_id or not receiver_id or not delivery_address_id or not description or not status:
            raise ValueError("All fields are required.")
        
        try:
            new_package = PackagesDAO.create(sender_id, receiver_id, delivery_address_id, description, status)
            return new_package
        except Exception as e:
            raise Exception(f"Error adding package: {str(e)}")

    @staticmethod
    def update_package(package_id, description, status):
      
        package = PackagesDAO.get_by_id(package_id)
        if not package:
            raise ValueError("Package not found.")

      
        if description is not None:
            package.description = description
        if status is not None:
            package.status = status
        
        try:
            PackagesDAO.update(package)
            return package
        except Exception as e:
            raise Exception(f"Error updating package: {str(e)}")

    @staticmethod
    def delete_package(package_id):
        # Перевірка існування пакета
        package = PackagesDAO.get_by_id(package_id)
        if not package:
            raise ValueError("Package not found.")

        try:
            PackagesDAO.delete(package_id)
        except Exception as e:
            raise Exception(f"Error deleting package: {str(e)}")

    @staticmethod
    def get_all_packages_with_receivers():
        """Отримання всіх пакунків з інформацією про отримувачів."""
        try:
            packages_with_receivers = PackagesDAO.get_all_with_receivers()
            result = []
            for package, receiver in packages_with_receivers:
                result.append({
                    "package_id": package.package_id,
                    "description": package.description,
                    "status": package.status,
                    "receiver_name": receiver.name,
                    "receiver_phone": receiver.phone,
                    "receiver_email": receiver.email
                })
            return result
        except Exception as e:
            raise Exception(f"Error retrieving packages with receivers: {str(e)}")
        
    def get_all_packages_with_senders():
        """Отримання всіх пакунків з інформацією про відправників."""
        try:
            packages_with_senders = PackagesDAO.get_all_with_senders()
            result = []
            for package, sender in packages_with_senders:
                result.append({
                    "package_id": package.package_id,
                    "description": package.description,
                    "status": package.status,
                    "sender_name": sender.full_name,
                    "sender_phone": sender.phone,
                    "sender_email": sender.email
                })
            return result
        except Exception as e:
            raise Exception(f"Error retrieving packages with senders: {str(e)}")