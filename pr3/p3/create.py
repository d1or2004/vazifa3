from base import Database


def created_table():
    work_type = f"""
        CREATE TABLE work_type(
            work_type_id SERIAL PRIMARY KEY,
            name VARCHAR(50));"""

    company = f"""
            CREATE TABLE company(
                company_id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                create_date DATE);"""

    categories = f"""
                CREATE TABLE categories(
                    categories_id SERIAL PRIMARY KEY,
                    name VARCHAR(50),
                    create_date DATE);"""

    regions = f"""
                    CREATE TABLE regions(
                        regions_id SERIAL PRIMARY KEY,
                        name VARCHAR(50),
                        create_date DATE);"""

    district = f"""
            CREATE TABLE district(
                district_id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                region_id INT REFERENCES regions(regions_id),
                create_date DATE);"""

    product = f"""
            CREATE TABLE product(
                product_id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                description TEXT,
                term TIMESTAMP DEFAULT now(),
                company_id INT REFERENCES company(company_id),
                categories_id INT REFERENCES categories(categories_id),
                price VARCHAR(50),
                create_date DATE);"""

    payment_type = f"""
            CREATE TABLE payment_type(
                payment_type_id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                create_date DATE);"""

    check = f"""
            CREATE TABLE check1(
                check_id SERIAL PRIMARY KEY,
                product_id INT REFERENCES product(product_id),
                product_summ VARCHAR(50),
                last_update TIMESTAMP DEFAULT now());"""

    kassa = f"""
                        CREATE TABLE kassa(
                            kassa_id SERIAL PRIMARY KEY,
                            check_id INT REFERENCES check1(check_id),
                            payment_type_id INT REFERENCES payment_type(payment_type_id),
                            last_update TIMESTAMP DEFAULT now());"""

    workers = f"""
                        CREATE TABLE workers(
                            workers_id SERIAL PRIMARY KEY,
                            first_name VARCHAR(20),
                            last_name VARCHAR(20),
                            phone_nomber VARCHAR(20),
                            home_address VARCHAR(20),
                            regions_id INT REFERENCES regions(regions_id),
                            work_type_id INT REFERENCES work_type(work_type_id),
                            last_update TIMESTAMP DEFAULT now());"""

    data_table = {
        "work_type": work_type,
        "company": company,
        "categories": categories,
        "regions": regions,
        "district": district,
        "product": product,
        "payment_type": payment_type,
        "check": check,
        "kassa": kassa,
        "workers": workers,
    }

    for i in data_table:
        print(f"{i} {Database.connect(data_table[i], "create")}")

#
# if __name__ == "__main__":
#     created_table()
