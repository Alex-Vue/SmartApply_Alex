/*
- Add script to each bin collider (an empty GO with a box collider component per assignment directions)
- Make the assignments below in the Unity editor
- Adjust script if needed
*/

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class Bin : MonoBehaviour
{
    //ASSIGN IN INSPECTOR
    public GameObject food;
    public int max_serving = 1; // Discrete or continuous food item?
    public int max_allowed = 250; // How many should be within the bin?

    //Assigned within script
    public GameObject bin; // script should be a component of the bin GO
    public List<GameObject> in_bin;
    public bool is_full;
    public bool is_filling;
    public Vector3 drop_point; // Vector3 is a data type holding three floats, often used to describe x,y,z position
    public Bounds bin_B; // Bounds are an invisible bounding rectangle surrounding a collider shape
    public Vector3 bin_center;

    //-------------------------------------------------------

    void Start()
    {
        bin = gameObject;
        is_filling = false;
        is_full = false;
        in_bin = new List<GameObject>();

        bin_B = bin.GetComponent<Collider>().bounds;
        bin_center = bin.GetComponent<Collider>().bounds.center; // the geometric center of a bounding rectangle surrounding the collider shape
        drop_point = new Vector3(bin_center.x, bin_B.center.y + bin_B.size.y / 4, bin_center.z); // dropped from above to allow food items to settle into the bins; Y VALUE MAY NEED ADJUSTMENT    
        StartCoroutine(Monitor_Bins()); // can be set up to start endless loop that fills food bins
    }

    //-------------------------------------------------------

    public IEnumerator Populate_Bin()
    {
        is_full = false;
        is_filling = true;

        while (is_full == false || in_bin.Count <= max_allowed)
        {
            //Make new food item
            GameObject new_food = Instantiate(food, bin.transform);
            new_food.transform.position = drop_point;
            in_bin.Add(new_food);
            food = new_food;

            //Check all items fit in the bin
            foreach (GameObject food in in_bin)
            {
                if(!bin_B.Intersects(food.GetComponent<Collider>().bounds)) // if the food and bin bounding boxes do not intersect...
                {
                    is_full = true; //...food has started to overflow the bin and we should stop adding new food

                    //Optionally, could remove any food items that overflow

                    //in_bin.Remove(new_food);
                    //Destroy(new_food);
                }
            }

            yield return null;
        }

        is_filling = false;

        // Watch for empty bins and refill them as needed
        StartCoroutine(Monitor_Bins());
    }

    //-------------------------------------------------------

    public IEnumerator Monitor_Bins()
    {
        while(in_bin.Count >= max_serving && is_filling == false) // if the amount in the bin goes below one serving while not currently refilling...
        {
            yield return null;
        }

        StartCoroutine(Populate_Bin()); // ...fill the bin back up
    }

    //-------------------------------------------------------

}// CLOSE CLASS














