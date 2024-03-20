using MySqlConnector;

using var connection = new MySqlConnection("Server=localhost;User ID=toor;Password=ZAQ!2wsx;Database=Database");
connection.Open();

using var command = new MySqlCommand("SELECT field FROM table;", connection);
using var reader = command.ExecuteReader();
while (reader.Read())
    Console.WriteLine(reader.GetString(0));

namespace Baza_danych_GUI_C_
{


    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }
    }
}
