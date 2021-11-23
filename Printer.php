
<?php

class Printer
{
  public $id;
	public $name;
  public $model;
	public $IP;

  public $CToner;
  public $MToner;
  public $YToner;
  public $KToner;

	public $AllPages;
	public $PagesBW;
	public $PagesColor;

	function __construct($printerArr)
	{
		$this->id = $printerArr["id"];
		$this->name = $printerArr["name"];
    $this->model = $printerArr["model"];
		$this->IP = $printerArr["IP"];

    $this->CToner = new Toner($printerArr["C"]);
    $this->MToner = new Toner($printerArr["M"]);
    $this->YToner = new Toner($printerArr["Y"]);
    $this->KToner = new Toner($printerArr["K"]);

		$this->AllPages = $printerArr["AllPages"];
    //$this->AllPages = Formater::FormatPageNumber($this->AllPages);
		$this->PagesBW = $printerArr["PagesBW"];
    //$this->PagesBW = Formater::FormatPageNumber($this->PagesBW);
		$this->PagesColor = $printerArr["PagesColor"];
    //$this->PagesColor = Formater::FormatPageNumber($this->PagesColor);
	}
}



?>