using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Newtonsoft.Json;
namespace Logi_Gui
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {



        }

    private void load_button_Click(object sender, EventArgs e)
    {
        string jsonFilePath = "C:\\Users\\xxx\\Baza danych\\python\\Praktyki 2024\\tcp server\\Logi-GUI-C#\\Logi-Gui\\output.json";
        var jsonData = System.IO.File.ReadAllText(jsonFilePath);
    
        //Teraz trzeba utworzyć listę obiektów do przechowywania danych z pliku JSON
        var items = JsonConvert.DeserializeObject<List<Item>>(jsonData);

        foreach(var item in items)
        {
            ListViewItem listItem = new ListViewItem(new[] {item.index, item.data, item.time, item.result});
            lista.Items.Add(listItem);
        }
    }

    //Create Item class to hold JSON Data
    public class Item
    {
        public string index { get; set; }
        public string data { get; set; }
        public string time { get; set; }
        public string result { get; set; }
    }

        private void lista_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}
