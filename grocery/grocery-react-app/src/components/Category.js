import React , { useEffect, useState } from 'react';
import axios from 'axios';


const Category = () => {

    const [category, setCategory] = useState('');
    const [subCategory, setSubCategory] = useState('');
    const [subCategories, setSubCategories] = useState('');


    // const [categories, setAllCat] = useState([]);

    useEffect(() => {
        if (category) {
            axios.get('http://127.0.0.1:8000/grocery_app/grocery/')
                .then(response => {
                    // Extract only the keys (id) from the response
                    let categ = [];
                    if (category.toLowerCase() === 'fruits') {
                         categ = response.data.map((item) => item.fruits);
                        
                    }
                    else if (category.toLowerCase() === 'oil') {
                         categ = response.data.map((item) => item.oil);
                       
                    }
                    else if (category.toLowerCase() === 'vegetables') {
                         categ = response.data.map((item) => item.vegetables);
                       
                    }
                    setSubCategories(categ);
                    console.log(categ);
                
                    // setAllCat(categ);
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });
        }
    },[category]
    );




    const categories = ['Fruits', 'Vegetables', 'Oil'];
   

    const hangleOnChangeCat = (event) => {
        setCategory(event.target.value);
        setSubCategory('');
        console.log(event.target.value);
    }

    const changeSub = (event) => {
        setSubCategory(event.target.value);

    }

    return (
        <div>
            <p> Dropdowns </p>
            <br></br>
            {/* <label value='category'> Choose something you need</label> */}
            <select name='category' id='category' onChange={hangleOnChangeCat} value={category}>
                <option selected> -- Select one --</option>
                {categories.length > 0 &&
                    categories.map((value, index) => (
                        <option key={index} value={value} >{ value }</option>
                    ))
                }
                
            </select>



            <p> The value you selected is : {category}</p>
            
            <select name='subcat' onChange={changeSub} value={subCategory}>
                <option selected> -- Select one --</option>
                {category &&
                    subCategories.length > 0 &&
                    subCategories.map((value, index) => (
                        <option key={index} value={value}>{value}</option>
                    ))
                }
            </select>
            <p>The subCatory you have chosen is { subCategory}</p>
        </div>
        
    );
}

export default Category;