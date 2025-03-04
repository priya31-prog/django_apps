import { useState } from 'react';

const Category = () => {

    const [category, setCategory] = useState('');
    const [subCategory, setSubCategory] = useState('');

    const categories = ['Fruits', 'Vegetables', 'Oil'];
    const subCategories = {
        'Fruits': [
            'Apple',
            'Banana', 'Grapes', 'Cherry',
        ],
        'Vegetables': [
            'Carrot', 'Betroot', 'Cucumber', 'Onion',
        ],
        'Oil': [
            'Coconut Oil', 'Olive Oil', 'Sunflower Oil',
        ]
    };

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
            <select name='category' id='category' onChange={hangleOnChangeCat} value ={category}>
                {categories != null &&
                    categories.map((value, index) => (
                        <option key={index} value={value} >{ value }</option>
                    ))
                }
                
              
            
            </select>
            <p> The value you selected is : {category}</p>
            
            <select name='subcat' onChange={ changeSub} value ={subCategory}>
                {category &&
                    subCategories[category] &&
                    subCategories[category].map((value, index) => (
                        <option key={index} value={value}>{value}</option>
                    ))
                }
            </select>
            <p>The subCatory you have chosen is { subCategory}</p>
        </div>
        
    );
}

export default Category;